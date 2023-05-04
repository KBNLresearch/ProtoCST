const saveDialogButton = document.getElementById("save-corpus");
const saveDialog = document.getElementById("save-dialog");
const saveButton = document.getElementById("save");
const cancelButton = document.getElementById("cancel");
saveDialog.returnValue = "corpus name"


// Save corpus button opens a modal dialog
saveDialogButton.addEventListener("click", () => {
  saveDialog.showModal();
});


// Form cancel button closes the dialog box
cancelButton.addEventListener("click", () => {
  console.log('Saving corpus was cancelled.')
  saveDialog.close("corpusNotSaved");
});

// Form cancel button closes the dialog box
$('#save').click(function() {
  $.post('save-corpus',
  {
    name: $('#corpus-name').val(),
    description: $('#corpus-description').val(),
    query: "[]",
    documents: "[]",
  },
  function(data, status){
    alert("Data: " + data + "\nStatus: " + status);
    saveDialog.close("corpusWasSaved");
  });
});

