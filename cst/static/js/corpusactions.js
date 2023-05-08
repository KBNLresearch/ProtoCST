
$(document).ready(function() {

  // Delete button deletes the corpus (ajax call to backend)
  $('.delete').click(function() {
    // TODO: dialog "Are you sure you want to delete corpus?" Alternative: install rubbish bin
    var corpusid = $(this).attr('data-id');
    var corpuscard = $('.corpuscard[data-id='+corpusid+']'); // Am I selecting the right corpus card??
    console.log('Delete corpus '+corpusid);
    console.log('Corresponding corpus card '+corpuscard+ corpuscard.attr('data-id'));
    corpuscard.css("color","yellow");
    corpuscard.css("border", "5px solid red");
    $.post('delete-corpus',
    {
      corpusid: corpusid,
    },
    function(data, status){
      alert("Data: " + data + "\nStatus: " + status);
      corpuscard.remove() // Why is this not working??
    });
  });
  });