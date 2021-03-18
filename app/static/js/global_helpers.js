function load_modal_dialog(elem_id) {
  var modal = document.getElementById(elem_id);
  modal.style.display = "block";
  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }
};

function close_modal_dialog(elem_id) {
  var modal = document.getElementById(elem_id);
  if (modal) {
    modal.style.display = "none";
  }
}
