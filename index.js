const express = require("express");
// const bodyParser = require("body-parser");
// const cors = require("cors");
const axios = require("axios");
const sha256 = require("sha256");
const uniqid = require("uniqid");
const port = 3002;
const app = express();

const PHONE_PE_HOST_URL = " https://api-preprod.phonepe.com/apis/pg-sandbox";
const MERCHANT_ID = "PGTESTPAYUAT";
const SALT_INDEX = 1;
const SALT_KEY = "099eb0cd-02cf-4e2a-8aca-3e6c6aff0399";
// const APP_BE_URL = "http://localhost:3002";

app.get("/", (req, res) => {
  res.send("Phonepe Is Working");
});

app.get("/pay", (req, res) => {
  const payEndpoint = "/pg/v1.pay";
  const merchantTransactionId = uniqid();
  const userId = 123;

  const payload = {
    merchantId: MERCHANT_ID,
    merchantTransactionId: merchantTransactionId,
    merchantUserId: userId,
    amount: 300,
    redirectUrl: `https://localhost:3002/redirect-url/${merchantTransactionId}`,
    // redirectUrl: `${APP_BE_URL}/redirect-url/${merchantTransactionId}`,
    redirectMode: "REDIRECT",
    mobileNumber: "9999999999",
    paymentInstrument: {
      type: "PAY_PAGE",
    },
  };

  //    SHA256(base64 encoded payload + "/pg/v1/pay" + salt key) + ### + salt index
  const bufferObj = Buffer.from(JSON.stringify(payload), "utf8");
  const base64EncodedPayload = bufferObj.toString("base64");
  const xVerify =
    sha256(base64EncodedPayload + payEndpoint + SALT_KEY) + "###" + SALT_INDEX;

  const options = {
    method: "post",
    url: `${PHONE_PE_HOST_URL}${payEndpoint}`,
    headers: {
      accept: "application/json",
      "Content-Type": "application/json",
       "X-VERIFY": xVerify,
    },
    data: {
      request: base64EncodedPayload,
    },
  };
  axios
    .request(options)
    .then(function (response) {
      console.log(response.data);
      res.send(response.data);
    })
    .catch(function (error) {
      console.error(error);
    });
});

app.listen(port, () => {
  console.log(`App Started listening on port ${port}`);
});
