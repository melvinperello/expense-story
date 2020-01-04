$( document ).ready(function() {

  $('a[href="#delete_fund"]').click(function(){
    let element = this;
    let tr_element = $(element).parent().parent();
    let params = JSON.parse(this.dataset['params']);
    let id = params._id
    // replace last character with id
    let http_url = params._call.replace(/.$/ , id)

    $.ajax({
      url: http_url,
      type: "DELETE",
      beforeSend: function(jqXHR, settings){
        console.log('start load')
      }
    }).done(function( data, textStatus, jqXHR ) {
      // remove row upon success callback
      $(tr_element).remove()
    }).fail(function( jqXHR, textStatus, errorThrown ) {
      console.log(jqXHR)
      console.log(textStatus)
      console.log(errorThrown)
    }).always(function( data, textStatus, errorThrown ) {
      console.log('end load')
    })




  });
});
