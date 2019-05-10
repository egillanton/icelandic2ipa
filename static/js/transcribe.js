var icelandicTextArea = $( "#icelandicText" );
var transcribedTextArea = $( "#transcribedText" );

$( "#transcribeButton" ).on( "click", function( event ) {
    var icelandicText = icelandicTextArea.val();
  $.ajax({
      url: "/transcribe",
      data: {
          icelandicText: icelandicText
      },
      success: function( result ) {
          transcribedTextArea.val(result.transcribedText)
      }
    });
});