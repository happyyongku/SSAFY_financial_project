<template>
    <div class="container custom-border p-4">
      <div class="row">
        <div class="col-lg-12 text-center mb-4">
          <h1 class="ercword">신혼 여행을 위한 환율 계산기</h1>
          <p>환율을 얻을 통화와 금액을 선택합니다</p>
        </div>
      </div>
      <div class="row justify-content-center">
        <div class="col-lg-12">
          <div class="custom-border p-3 mb-3">
            <h5 class="text-center mb-3">바꾸고 싶은 통화</h5>
            <div class="row">
              <div class="col-lg-6">
                <div class="input-group mb-3">
                  <span class="input-group-text" id="inputGroup-sizing-default">Amount</span>
                  <input type="number" id="amount-one" class="form-control" aria-describedby="inputGroup-sizing-default" value="1">
                </div>
              </div>
              <div class="col-lg-6">
                <select class="form-select" name="currency-one" id="currencyOne">
                    <option value="AED">AED</option>
                    <option value="ARS">ARS</option>
                    <option value="AUD">AUD</option>
                    <option value="BGN">BGN</option>
                    <option value="BRL">BRL</option>
                    <option value="BSD">BSD</option>
                    <option value="CAD">CAD</option>
                    <option value="CHF">CHF</option>
                    <option value="CLP">CLP</option>
                    <option value="CNY">CNY</option>
                    <option value="COP">COP</option>
                    <option value="CZK">CZK</option>
                    <option value="DKK">DKK</option>
                    <option value="DOP">DOP</option>
                    <option value="EGP">EGP</option>
                    <option value="EUR">EUR</option>
                    <option value="FJD">FJD</option>
                    <option value="GBP">GBP</option>
                    <option value="GTQ">GTQ</option>
                    <option value="HKD">HKD</option>
                    <option value="HRK">HRK</option>
                    <option value="HUF">HUF</option>
                    <option value="IDR">IDR</option>
                    <option value="ILS">ILS</option>
                    <option value="INR">INR</option>
                    <option value="ISK">ISK</option>
                    <option value="JPY">JPY</option>
                    <option value="KRW">KRW</option>
                    <option value="KZT">KZT</option>
                    <option value="MXN">MXN</option>
                    <option value="MYR">MYR</option>
                    <option value="NOK">NOK</option>
                    <option value="NZD">NZD</option>
                    <option value="PAB">PAB</option>
                    <option value="PEN">PEN</option>
                    <option value="PHP">PHP</option>
                    <option value="PKR">PKR</option>
                    <option value="PLN">PLN</option>
                    <option value="PYG">PYG</option>
                    <option value="RON">RON</option>
                    <option value="RUB">RUB</option>
                    <option value="SAR">SAR</option>
                    <option value="SEK">SEK</option>
                    <option value="SGD">SGD</option>
                    <option value="THB">THB</option>
                    <option value="TRY">TRY</option>
                    <option value="TWD">TWD</option>
                    <option value="UAH">UAH</option>
                    <option value="USD" selected>USD</option>
                    <option value="UYU">UYU</option>
                    <option value="VND">VND</option>
                    <option value="ZAR">ZAR</option>
                </select>
              </div>
            </div>
          </div>
          <div class="custom-border p-3">
            <h5 class="text-center mb-3">바꾸려는 통화</h5>
            <div class="row">
              <div class="col-lg-6">
                <div class="input-group mb-3">
                  <span class="input-group-text" id="inputGroup-sizing-default">Amount</span>
                  <input type="number" id="amount-two" class="form-control" aria-describedby="inputGroup-sizing-default" value="1">
                </div>
              </div>
              <div class="col-lg-6">
                <select class="form-select" name="currency-two" id="currencyTwo">
                    <option value="AED">AED</option>
                    <option value="ARS">ARS</option>
                    <option value="AUD">AUD</option>
                    <option value="BGN">BGN</option>
                    <option value="BRL">BRL</option>
                    <option value="BSD">BSD</option>
                    <option value="CAD">CAD</option>
                    <option value="CHF">CHF</option>
                    <option value="CLP">CLP</option>
                    <option value="CNY">CNY</option>
                    <option value="COP">COP</option>
                    <option value="CZK">CZK</option>
                    <option value="DKK">DKK</option>
                    <option value="DOP">DOP</option>
                    <option value="EGP">EGP</option>
                    <option value="EUR">EUR</option>
                    <option value="FJD">FJD</option>
                    <option value="GBP">GBP</option>
                    <option value="GTQ">GTQ</option>
                    <option value="HKD">HKD</option>
                    <option value="HRK">HRK</option>
                    <option value="HUF">HUF</option>
                    <option value="IDR">IDR</option>
                    <option value="ILS">ILS</option>
                    <option value="INR">INR</option>
                    <option value="ISK">ISK</option>
                    <option value="JPY">JPY</option>
                    <option value="KRW">KRW</option>
                    <option value="KZT">KZT</option>
                    <option value="MXN">MXN</option>
                    <option value="MYR">MYR</option>
                    <option value="NOK">NOK</option>
                    <option value="NZD">NZD</option>
                    <option value="PAB">PAB</option>
                    <option value="PEN">PEN</option>
                    <option value="PHP">PHP</option>
                    <option value="PKR">PKR</option>
                    <option value="PLN">PLN</option>
                    <option value="PYG">PYG</option>
                    <option value="RON">RON</option>
                    <option value="RUB">RUB</option>
                    <option value="SAR">SAR</option>
                    <option value="SEK">SEK</option>
                    <option value="SGD">SGD</option>
                    <option value="THB">THB</option>
                    <option value="TRY">TRY</option>
                    <option value="TWD">TWD</option>
                    <option value="UAH">UAH</option>
                    <option value="USD" selected>USD</option>
                    <option value="UYU">UYU</option>
                    <option value="VND">VND</option>
                    <option value="ZAR">ZAR</option>
                </select>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="row justify-content-center">
        <div class="col-lg-8 text-center">
          <div class="d-flex align-items-center justify-content-center">
            <button id="swap" class="btn btn-primary me-3">Swap</button>
            <div id="rate" class="rate"></div>
          </div>
        </div>
      </div>
    </div>
  </template>
  

<script setup>
document.addEventListener("DOMContentLoaded", () => {
  const currencyOne = document.getElementById("currencyOne");
  const amountOne = document.getElementById("amount-one");
  const swap = document.getElementById("swap");
  const rate = document.getElementById("rate");
  const currencyTwo = document.getElementById("currencyTwo");
  const amountTwo = document.getElementById("amount-two");

  // 환율 업데이트

  const updateCurrency = async () => {
    const url = await fetch(
      `https://v6.exchangerate-api.com/v6/52f1f656328d5996e352de41/latest/${currencyOne.value}`
    );

    data = await url.json();

    rate.innerText = "1 " + currencyOne.value + " = " + data.conversion_rates[currencyTwo.value] + currencyTwo.value;

    amountTwo.value = (
      amountOne.value * data.conversion_rates[currencyTwo.value]
    ).toFixed(2);
  };

  // 환율 서로 바꾸기

  function changeCurrency() {
    let temp;

    temp = currencyTwo.value;

    currencyTwo.value = currencyOne.value;
    currencyOne.value = temp;
    updateCurrency();
  }

  updateCurrency();

  currencyOne.addEventListener("change", updateCurrency);
  currencyTwo.addEventListener("change", updateCurrency);
  amountOne.addEventListener("input", updateCurrency);
  swap.addEventListener("click", changeCurrency);
});

</script>

<style scoped>
*{
    box-sizing: border-box;
}
body{
    margin: 0;
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    flex-direction: column;
    background-color: #fff;
}


.img{
    width: 150px;
    height: 150px;
}

.ercword{
    color: #D6B534;
}

.currency{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 40px 0;
}

.currency input{
    text-align: right;
    padding: 1px 2px;
    border: none;
    font-size: 30px;
}

.selectcurrency{
    padding: 10px 20px 10px 10px;
    font-size: 16px;
    border-radius: 10px;
    border: 1px solid #777;
    background: transparent;

}

.swap-rate-container{
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.rate {
    color: #5fbaa7;
    font-size: 18px;
    padding: 0 10px;
  }



.btn{
    background-color: #5fbaa7;
    color: #fff;
    padding: 5px 12px;
    border-radius: 10px;
}

.custom-border {
  border: 2px solid #D6B534;
}
</style>