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
});
