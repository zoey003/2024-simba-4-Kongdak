const backBtn = document.querySelector("#back");
const homeBtn = document.querySelector("#home");

homeBtn.addEventListener("click", () => {
  window.location.href = "/mainpage";
});

backBtn.addEventListener("click", () => {
  window.history.back();
});
