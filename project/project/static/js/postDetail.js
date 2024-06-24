const back = document.getElementById("back_edit");

back.addEventListener("click", () => {
  window.location.href = localStorage.getItem("detailBack");
  console.log("c,ci");
});
const editBtn = document.getElementById("edit_diary");
const deleteBtn = document.getElementById("delete_diary");
const deleteModal = document.getElementById("delete-modal");
const confirmDelete = document.getElementById("confirm-delete");
const cancelDelete = document.getElementById("cancel-delete");
const contentToBlur = document.querySelectorAll("#root > *:not(#delete-modal)");
const searchBtn = document.querySelector("#edit_textarea");

function toggleBlur(toggle) {
  contentToBlur.forEach((element) => {
    if (toggle) {
      element.classList.add("blurred");
    } else {
      element.classList.remove("blurred");
    }
  });
}

deleteBtn.addEventListener("click", () => {
  deleteModal.classList.remove("hidden-class");
  toggleBlur(true);
});

searchBtn.addEventListener("click", function () {
  deleteModal.classList.add("hidden-class");
  toggleBlur(false);
});

confirmDelete.addEventListener("click", function () {
  window.location.href = deleteUrl;
});

cancelDelete.addEventListener("click", function () {
  window.location.href = detailpostUrl;
});

editBtn.addEventListener("click", function () {
  window.location.href = editUrl;
});
