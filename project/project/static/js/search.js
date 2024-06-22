document.addEventListener("DOMContentLoaded", function () {
  const searchNone = document.getElementById("search_none");
  const searchFrame = document.querySelector(".search_frame1");

  // 검색 결과가 없으면 search_none div를 표시
  if (searchFrame.children.length === 1) {
    // search_frame1 안에 아무것도 없을 때
    searchNone.style.display = "block";
  } else {
    searchNone.style.display = "none";
  }

  const searchBtn = document.getElementById("search_img");
  searchBtn.addEventListener("click", () => {
    window.location.href = searchUrl;
  });
});

const tagInput = document.querySelector("#tag-zone");
// 한글 입력 상태 확인 변수
let isComposing = false;

tagInput.addEventListener("compositionstart", () => {
  isComposing = true;
});

tagInput.addEventListener("compositionend", () => {
  isComposing = false;
});

tagInput.addEventListener("keydown", function (event) {
  if (event.key === "Enter" && !isComposing) {
    event.preventDefault();
    const tagValue = tagInput.value.trim();
    if (tagValue && !tagValue.endsWith("#")) {
      const tags = tagInput.value.trim().split(" ");
      let lastTag = tags.pop();

      if (!lastTag.startsWith("#")) {
        lastTag = `#${lastTag}`;
      }

      if (!tags.includes(lastTag) && lastTag !== "#") {
        tags.push(lastTag);
      }

      tagInput.value = tags.join(" ") + " ";
    }
    validateInputs();
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const postFrames = document.querySelectorAll(".search_place");

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
});
