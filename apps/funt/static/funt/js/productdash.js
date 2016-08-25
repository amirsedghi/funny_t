$(document).ready(function(){
  $('input[type="checkbox"]').click(function(){
    if($('#same').prop('checked') == true){
      $('#pf').val($('#sf').val());
      $('#pl').val($('#sl').val());
      $('#pa').val($('#sa').val());
      $('#pa2').val($('#sa2').val());
      $('#pc').val($('#sc').val());
      $('#ps').val($('#ss').val());
      $('#pz').val($('#sz').val());
      $('#b-info').slideUp('slow', function(){});
    }
    else if($('#same').prop('checked') == false){
      $('#pf').val('');
      $('#pl').val('');
      $('#pa').val('');
      $('#pa2').val('');
      $('#pc').val('');
      $('#ps').val('');
      $('#pz').val('');
      $('#b-info').slideDown('slow', function(){});
    }
  })

})
