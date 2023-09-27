const fetch = require("node-fetch");

async function api(method, endpoint, body = null) {
  json = {
    method: method,
    headers: {
      "Content-Type": "application/json",
    },
  };
  if (body) {
    json.body = JSON.stringify(body);
  }

  const response = await fetch(`http://127.0.0.1:8000/${endpoint}`, json);
  console.log(response);
  const data = await response.json();
  console.log(data);
}

async function main() {
  await api("POST", "add", {
    payer: "DANNON",
    points: 300,
    timestamp: "2022-10-31T10:00:00Z",
  });

  await api("POST", "add", {
    payer: "UNILEVER",
    points: 200,
    timestamp: "2022-10-31T11:00:00Z",
  });

  await api("POST", "add", {
    payer: "DANNON",
    points: -200,
    timestamp: "2022-10-31T15:00:00Z",
  });

  await api("POST", "add", {
    payer: "MILLER COORS",
    points: 10000,
    timestamp: "2022-11-01T14:00:00Z",
  });

  await api("POST", "add", {
    payer: "DANNON",
    points: 1000,
    timestamp: "2022-11-02T14:00:00Z",
  });

  await api("POST", "spend", {
    points: 5000,
  });

  await api("GET", "balance");
}

main();
