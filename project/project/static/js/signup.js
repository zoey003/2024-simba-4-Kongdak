const pw = document.querySelector("#password");
const pwCheck = document.querySelector("#confirm");
const pwInfo = document.querySelector("#password-info");
const pwCheckText = document.querySelector("#password-check");
const nickname = document.querySelector("#nickname");
const nameInfo = document.querySelector("#nickname-info");
const studentID = document.querySelector("#studentID");
const studentInfo = document.querySelector("#student-info");
const signupBtn = document.querySelector("#sign-up-submit");
const idTest = document.querySelector("#id-input");
const validCheckBtn = document.querySelector(".check-button");
const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
const idInfo = document.querySelector("#id-info");

const validPW = /^(?=.*[A-Za-z])(?=.*\d)[\w\d!@#$%^&*]{8,}$/;
const validName = /^[A-Za-z가-힣]{1,}$/;
const validStudentID = /^\d{10}$/;

let idStatus = false;
let pwStatus = false;
let confirmStatus = false;
let nameStatus = false;
let codeStatus = false;

function checkFormValidity() {
  if (idStatus && pwStatus && confirmStatus && nameStatus && codeStatus) {
    signupBtn.disabled = false;
    signupBtn.classList.add("abled-btn");
  } else {
    signupBtn.disabled = true;
    signupBtn.classList.remove("abled-btn");
  }
}

pw.addEventListener("input", () => {
  if (!validPW.test(pw.value)) {
    pw.classList.add("warning-input");
    pwInfo.classList.add("warning-text");
    pwStatus = false;
  } else {
    pw.classList.remove("warning-input");
    pwInfo.classList.remove("warning-text");
    pwStatus = true;
  }
  if (pw.value === pwCheck.value) {
    pwCheck.classList.remove("warning-input");
    pwCheckText.classList.remove("warning-text");
    pwCheckText.classList.add("hidden-class");
    confirmStatus = true;
  } else {
    pwCheck.classList.add("warning-input");
    pwCheckText.classList.add("warning-text");
    pwCheckText.classList.remove("hidden-class");
    confirmStatus = false;
  }
  checkFormValidity();
});

pwCheck.addEventListener("input", () => {
  if (pw.value === pwCheck.value) {
    pwCheck.classList.remove("warning-input");
    pwCheckText.classList.remove("warning-text");
    pwCheckText.classList.add("hidden-class");
    confirmStatus = true;
  } else {
    pwCheck.classList.add("warning-input");
    pwCheckText.classList.add("warning-text");
    pwCheckText.classList.remove("hidden-class");
    confirmStatus = false;
  }
  checkFormValidity();
});

nickname.addEventListener("input", () => {
  if (validName.test(nickname.value)) {
    nickname.classList.remove("warning-input");
    nameInfo.classList.remove("warning-text");
    nameInfo.classList.add("hidden-class");
    nameStatus = true;
  } else {
    nickname.classList.add("warning-input");
    nameInfo.classList.add("warning-text");
    nameInfo.classList.remove("hidden-class");
    nameStatus = false;
  }
  checkFormValidity();
});

studentID.addEventListener("input", () => {
  if (validStudentID.test(studentID.value)) {
    studentID.classList.remove("warning-input");
    studentInfo.classList.remove("warning-text");
    studentInfo.classList.add("hidden-class");
    codeStatus = true;
  } else {
    studentID.classList.add("warning-input");
    studentInfo.classList.add("warning-text");
    studentInfo.classList.remove("hidden-class");
    codeStatus = false;
  }
  checkFormValidity();
});

validCheckBtn.addEventListener("click", (event) => {
  event.preventDefault();

  fetch(`/check_username/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
      "X-Requested-With": "XMLHttpRequest",
    },
    body: JSON.stringify({ username: idTest.value }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.is_taken) {
        idInfo.classList.remove("hidden-class");
        idInfo.classList.add("warning-text");
        idInfo.classList.remove("valid-text");
        idInfo.textContent = "사용 중인 아이디입니다.";
        idStatus = false;
      } else {
        idInfo.classList.remove("hidden-class");
        idInfo.classList.add("valid-text");
        idInfo.classList.remove("warning-text");
        idTest.classList.add("valid-input");
        idInfo.textContent = "사용 가능한 아이디입니다.";
        idStatus = true;
      }
      checkFormValidity();
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
