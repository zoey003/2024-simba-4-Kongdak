const logoutBtn = document.querySelector(".logout-view > button");
const logoutModal = document.getElementById("logout-modal");
const confirmLogout = document.getElementById("confirm-logout");
const cancelLogout = document.getElementById("cancel-logout");
const contentToBlur = document.querySelectorAll("#root > *:not(#logout-modal)");
const searchBtn = document.querySelector(".search-view");
const collectionBtn = document.querySelector(".collection-view");

function getCurrentDate() {
  const today = new Date();
  const year = today.getFullYear();
  const month = String(today.getMonth() + 1).padStart(2, "0");
  const day = String(today.getDate()).padStart(2, "0");
  const weekdays = [
    "일요일",
    "월요일",
    "화요일",
    "수요일",
    "목요일",
    "금요일",
    "토요일",
  ];
  const weekday = weekdays[today.getDay()];
  return `${year}년 ${month}월 ${day}일 ${weekday}`;
}

function calculateDaysSinceSignup(signupDate) {
  const today = new Date();
  const signup = new Date(signupDate);
  const timeDifference = today.getTime() - signup.getTime();
  const daysDifference = Math.floor(timeDifference / (1000 * 3600 * 24));
  return daysDifference;
}

document.getElementById("today-view").textContent = getCurrentDate();

const signupDate = document
  .getElementById("sign-date-view")
  .textContent.replace(" 입학", "");
const daysSinceSignup = calculateDaysSinceSignup(signupDate);
document.getElementById("since-date-view").textContent = `+ ${
  daysSinceSignup + 1
}일 째 콩닥콩닥`;

function toggleBlur(toggle) {
  contentToBlur.forEach((element) => {
    if (toggle) {
      element.classList.add("blurred");
    } else {
      element.classList.remove("blurred");
    }
  });
}

logoutBtn.addEventListener("click", () => {
  logoutModal.classList.remove("hidden-class");
  toggleBlur(true);
});

cancelLogout.addEventListener("click", function () {
  logoutModal.classList.add("hidden-class");
  toggleBlur(false);
});

confirmLogout.addEventListener("click", function () {
  window.location.href = logoutUrl;
});

searchBtn.addEventListener("click", function () {
  window.location.href = searchUrl;
});

collectionBtn.addEventListener("click", () => {
  window.location.href = allPostUrl;
});

const postFrames = document.querySelectorAll(".place");

postFrames.forEach((frame) => {
  const category = frame.getAttribute("data-category");

  // 여기서 카테고리에 따라 스타일을 지정합니다.
  switch (category) {
    case "a":
      frame.style.backgroundColor = "#FE8535";
      frame.style.color = "white";
      break;
    case "b":
      frame.style.backgroundColor = "#D9D9D9";
      frame.style.color = "black";
      break;
    case "c":
      frame.style.backgroundColor = "white";
      frame.style.color = "black";
      frame.style.border = "solid 1px black";
      break;
    // 필요한 만큼 카테고리를 추가하십시오.
  }

  // post.category 숨기기
  const categoryDiv = frame.querySelector(".place");
  if (categoryDiv) {
    categoryDiv.style.display = "none";
  }
});
