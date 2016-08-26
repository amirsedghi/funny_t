$(document).ready(function(){
  $('#actions').finish().slideUp(0);
  $("#cat_ul").hover(
    function () {
        $('#actions').finish().slideDown('fast');
    },
    function () {
        $('#actions').finish().slideUp('fast');
    });
});
