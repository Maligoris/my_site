$(document).ready(function() {
  $(function() {  
    $('#menu_m').click(function() {
        $('.overlay').slideToggle(); // Добавляет свойство display: block и ставит none при повторном нажатии
    });
       
    $('#menu_m').on('click', function() {
        this.classList.toggle('active');
    });
  });  
});

