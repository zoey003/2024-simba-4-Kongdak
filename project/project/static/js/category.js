document.addEventListener("DOMContentLoaded", function () {
  const topAuthors = document.querySelectorAll(".category_1_top");
  const weatherList = document.querySelectorAll(".weather-list");
  const firstAuthorPostCount = topAuthors[0].getAttribute("data-post-count");

  topAuthors.forEach((author) => {
    const postCount = author.getAttribute("data-post-count");
    const fillBar = author.querySelector(".fill");
    const percentage = (postCount / firstAuthorPostCount) * 100;
    fillBar.style.width = percentage + "%";
  });

  weatherList.forEach((weather) => {
    let weatherImg = weather.querySelector(".weather-img");
    const weatherData = weather.getAttribute("weather-data");
    if (weatherData === "맑음") {
      weatherImg.setAttribute("src", sunnyUrl);
    } else if (weatherData === "구름낌") {
      weatherImg.setAttribute("src", cloudyUrl);
    } else if (weatherData === "흐림") {
      weatherImg.setAttribute("src", cloudyUrl);
    } else if (weatherData === "비") {
      weatherImg.setAttribute("src", umbrellaUrl);
    } else if (weatherData === "눈") {
      weatherImg.setAttribute("src", snowyUrl);
    }
    weatherImg.setAttribute("width", "25px");
  });
});
