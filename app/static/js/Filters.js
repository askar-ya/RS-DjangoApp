document.addEventListener('DOMContentLoaded', function () {
  var favItemsBtns = document.querySelectorAll('.fav-item__icon');
  favItemsBtns.forEach(function (btn) {
    btn.addEventListener('click', function (event) {
      var parent = btn.closest('.fav-item');

      // Закрываем все открытые элементы, кроме текущего
      favItemsBtns.forEach(function (otherBtn) {
        var otherParent = otherBtn.closest('.fav-item');
        if (otherParent && otherParent !== parent) {
          otherParent.classList.remove('is-open');
        }
      });

      // Открываем/закрываем текущий элемент
      parent.classList.toggle('is-open');
    });
  });
  document.addEventListener('click', function (event) {
    // Проверяем, был ли клик вне dropdown
    var drop = event.target.closest('.fav-item');
    if (!drop) {
      // Закрываем все открытые dropdowns
      favItemsBtns.forEach(function (menuButton) {
        var parentRow = menuButton.closest('.fav-item');
        if (parentRow && parentRow.classList.contains('is-open')) {
          parentRow.classList.remove('is-open');
        }
      });
    }
  });
});