$(document).ready(function(){
  $("#cat_ul").hover(
    function () {
        $('#actions').finish().slideDown('fast');
    },
    function () {
        $('#actions').finish().slideUp('fast');
    });
});
