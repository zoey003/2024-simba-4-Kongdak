const backBtn = document.querySelector("#back");

backBtn.addEventListener("click", () => {
  if (urlCase === "auto") {
    const url = window.location.href;

    // URL 객체를 생성하여 경로명을 추출합니다.
    const urlObject = new URL(url);
    const pathname = urlObject.pathname;

    // 경로명을 '/'로 분할하여 배열로 만듭니다.
    const pathSegments = pathname.split("/");
    console.log(pathSegments);

    // 첫 번째 세그먼트를 가져옵니다.
    const firstSegment = pathSegments[2];
    window.location.href = `/secondpage_${firstSegment}`;
  } else if (urlCase === "back") {
    window.history.back();
  } else if (urlCase === "detail") {
    window.location.href = localStorage.getItem("detailBack");
  } else {
    console.log("!");
    window.location.href = urlCase;
  }
});

// 현재 URL을 가져옵니다.

// 결과를 출력합니다.
