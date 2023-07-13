// Delete button deletes the corpus (ajax call to backend)
  $('.delete').click(function() {
    // TODO: dialog "Are you sure you want to delete corpus?" Alternative: install rubbish bin
    var corpusid = $(this).attr('data-id');
    var corpuscard = $('#corpuscard-'+corpusid);
    $.post('delete-corpus',
    {
      corpusid: corpusid,
    },
    function(data, status){
      corpuscard.remove()
    });
  });
  });