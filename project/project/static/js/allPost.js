document.addEventListener("DOMContentLoaded", function () {
  const heartButtons = document.querySelectorAll(".heart-btn");
  const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  heartButtons.forEach((heartBtn) => {
    const heartImg = heartBtn.querySelector("img");
    const isBookmarked = heartImg.getAttribute("data-is_bookmarked") === "True";

    if (isBookmarked) {
      heartImg.setAttribute("src", redHeartUrl);
    } else {
      heartImg.setAttribute("src", whiteHeartUrl);
    }

    heartBtn.addEventListener("click", () => {
      if (heartImg.getAttribute("src") === whiteHeartUrl) {
        heartImg.setAttribute("src", redHeartUrl);
      } else {
        heartImg.setAttribute("src", whiteHeartUrl);
      }

      fetch(`/post/${heartBtn.getAttribute("data")}/bookmark/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
          "X-Requested-With": "XMLHttpRequest", // AJAX 요청을 명시적으로 표시
        },
        body: JSON.stringify({ id: heartBtn.getAttribute("data") }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            if (data.is_bookmarked) {
              heartImg.setAttribute("src", redHeartUrl);
            } else {
              heartImg.setAttribute("src", whiteHeartUrl);
            }
          } else {
            console.error("Failed to update the heart status");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  });

  //장소별색깔프레임지정

  const placeFrames = document.querySelectorAll(".place");

  placeFrames.forEach((frame) => {
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

  //작성한 글 없음을 표시
  const postNone = document.getElementById("post_none");
  const postFrame = document.querySelector(".post-view");

  if (!postFrame) {
    postNone.style.display = "block";
  } else {
    postNone.style.display = "none";
  }

  if (postFrame && postFrame.children.length === 1) {
    postNone.style.display = "block";
  } else {
    postNone.style.display = "none";
  }
});
