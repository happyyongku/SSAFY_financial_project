 <template>
  <div>
    <h1 class="ercword">내 집 주변 은행 검색</h1>
    <div class="container custom-border">
      <div id="map" class="map"></div>
      <div id="menu_wrap" class="bg_white">
        <div class="option">
          <div>
            <input type="text" id="keyword" size="15" placeholder="키워드 입력" class="custom-border" />
            <input type="text" id="region" size="15" placeholder="지역 입력" class="custom-border" />
            <button @click="searchPlaces" class="custom-border">검색하기</button>
            <button @click="toggleMapType" class="custom-border">지도 타입 변경</button>
          </div>
        </div>
        <ul id="placesList"></ul>
        <div id="pagination"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mapType: "normal" // 지도 형태 초기값은 일반 지도로 설정
    };
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap();
    } else {
      this.addKakaoMapScript();
    }
  },
  methods: {
    addKakaoMapScript() {
      const script = document.createElement("script");
      script.onload = () => kakao.maps.load(this.initMap);
      script.src = "https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=561a3affdd7415744010571e8695115c&libraries=services";
      document.head.appendChild(script);
    },
    initMap() {
      navigator.geolocation.getCurrentPosition(position => {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        const mapContainer = document.getElementById("map");
        const mapOption = {
          center: new kakao.maps.LatLng(latitude, longitude),
          level: 3,
          mapTypeId: kakao.maps.MapTypeId.ROADMAP // 초기 지도 타입 설정 (일반 지도)
        };

        this.map = new kakao.maps.Map(mapContainer, mapOption);
        this.ps = new kakao.maps.services.Places();
        this.infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
        this.markers = [];
      });
    },
    searchPlaces() {
      const keyword = document.getElementById("keyword").value.trim();
      const region = document.getElementById("region").value.trim(); // 지역 입력 값 가져오기

      if (!keyword || !region) {
        alert("키워드와 지역을 모두 입력해주세요!");
        return;
      }

      const query = keyword + ' ' + region; // 지역 정보를 키워드와 합침

      this.ps.keywordSearch(query, this.placesSearchCB.bind(this)); // 합친 쿼리로 검색 수행
    },
    placesSearchCB(data, status, pagination) {
      if (status === kakao.maps.services.Status.OK) {
        this.displayPlaces(data);
        this.displayPagination(pagination);
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alert("검색 결과가 존재하지 않습니다.");
      } else if (status === kakao.maps.services.Status.ERROR) {
        alert("검색 결과 중 오류가 발생했습니다.");
      }
    },
    displayPlaces(places) {
      const listEl = document.getElementById("placesList");
      const bounds = new kakao.maps.LatLngBounds();

      this.removeAllChildNodes(listEl);
      this.removeMarker();

      places.forEach((place, i) => {
        const placePosition = new kakao.maps.LatLng(place.y, place.x);
        const marker = this.addMarker(placePosition, i);
        const itemEl = this.getListItem(i, place);

        bounds.extend(placePosition);

        kakao.maps.event.addListener(marker, "mouseover", () => {
          this.displayInfowindow(marker, place.place_name);
        });

        kakao.maps.event.addListener(marker, "mouseout", () => {
          this.infowindow.close();
        });

        itemEl.onmouseover = () => {
          this.displayInfowindow(marker, place.place_name);
        };

        itemEl.onmouseout = () => {
          this.infowindow.close();
        };

        listEl.appendChild(itemEl);
      });

      this.map.setBounds(bounds);
    },
    getListItem(index, place) {
      const el = document.createElement("li");
      const itemStr = `
        <span class="markerbg marker_${index + 1}"></span>
        <div class="info">
          <h5>${index + 1}. ${place.place_name}</h5>
          <div>
            <span>${place.road_address_name ? place.road_address_name : place.address_name}</span>
          </div>
          <div>
            <span class="tel">${place.phone}</span>
          </div>
        </div>
      `;
      el.innerHTML = itemStr;
      el.className = "item";
      return el;
    },
    addMarker(position, idx) {
      const imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png";
      const imageSize = new kakao.maps.Size(36, 37);
      const imgOptions = {
        spriteSize: new kakao.maps.Size(36, 691),
        spriteOrigin: new kakao.maps.Point(0, idx * 46 + 10),
        offset: new kakao.maps.Point(13, 37),
      };
      const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions);
      const marker = new kakao.maps.Marker({
        position: position,
        image: markerImage,
      });

      marker.setMap(this.map);
      this.markers.push(marker);

      return marker;
    },
    removeMarker() {
      this.markers.forEach((marker) => marker.setMap(null));
      this.markers = [];
    },
    displayPagination(pagination) {
      const paginationEl = document.getElementById("pagination");

      this.removeAllChildNodes(paginationEl);

      for (let i = 1; i <= pagination.last; i++) {
        const el = document.createElement("a");
        el.href = "#";
        el.innerHTML = i;
        el.className = pagination.current === i ? "on" : "";
        el.onclick = () => {
          pagination.gotoPage(i);
        };
        paginationEl.appendChild(el);
      }
    },
    displayInfowindow(marker, title) {
      const content = `<div style="padding:5px;z-index:1;">${title}</div>`;
      this.infowindow.setContent(content);
      this.infowindow.open(this.map, marker);
    },
    removeAllChildNodes(el) {
      while (el.hasChildNodes()) {
        el.removeChild(el.lastChild);
      }
    },
    toggleMapType() {
      // 현재 지도의 타입 확인하여 스카이뷰이면 일반 지도로 변경, 일반 지도이면 스카이뷰로 변경
      this.mapType = this.mapType === "normal" ? "skyview" : "normal";
      this.map.setMapTypeId(this.mapType === "normal" ? kakao.maps.MapTypeId.ROADMAP : kakao.maps.MapTypeId.SKYVIEW);
    },
  },
};

</script>

<style>
.container {
  display: flex;
}
.map {
  width: 70%;
  height: 600px;
}
.bg_white {
  width: 30%;
  background: white;
  overflow-y: auto;
  height: 600px;
}
.option {
  padding: 10px 10px 0;
}
#placesList .item {
  padding: 10px;
  border-bottom: 1px solid #e2e2e2;
  line-height: 1.5; /* 줄 간격 조정 */
}
#placesList .info {
  margin-left: 10px; /* 정보 항목에 좌측 여백 추가 */
}
#placesList .tel {
  display: block; /* 전화번호를 별도의 줄로 표시 */
  margin-top: 5px; /* 상단 여백 추가 */
  color: #007bff; /* 전화번호 색상 변경 */
}
#pagination a {
  margin: 0 2px;
  padding: 3px 6px;
  border: 1px solid #e2e2e2;
  color: #333;
  text-decoration: none;
  cursor: pointer;
}
#pagination a.on {
  border-color: #007bff;
  color: #007bff;
}

.ercword{
    color: #D6B534;
}

.custom-border {
  border: 2px solid #D6B534;
  margin: 2px;
}
</style>