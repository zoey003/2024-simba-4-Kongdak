document.addEventListener("DOMContentLoaded", function () {
  const weatherZone = document.querySelector("#weather-zone");
  const weatherData = weatherZone.getAttribute("weather-data");
  const weatherImg = document.querySelector("#weather-img");

  if (weatherData === "맑음") {
    weatherImg.setAttribute("src", sunnyUrl);
  } else if (weatherData === "구름낌") {
    weatherImg.setAttribute("src", cloudyUrl);
  } else if (weatherData === "비") {
    weatherImg.setAttribute("src", umbrellaUrl);
  } else if (weatherData === "눈") {
    weatherImg.setAttribute("src", snowyUrl);
  } else {
    weatherImg.setAttribute("src", cloudUrl);
  }
  weatherImg.setAttribute("width", "25px");
});
