$(document).ready(function(){
  $('#actions').finish().slideUp('fast');
  $("#cat_ul").hover(
    function () {
        $('#actions').finish().slideDown('fast');
    },
    function () {
        $('#actions').finish().slideUp('fast');
    });
});
