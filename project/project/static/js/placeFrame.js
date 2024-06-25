const postFrames = document.querySelectorAll(".place");

postFrames.forEach((frame) => {
  const category = frame.getAttribute("data-category");

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
  }

  // post.category 숨기기
  const categoryDiv = frame.querySelector(".place");
  if (categoryDiv) {
    categoryDiv.style.display = "none";
  }
});
