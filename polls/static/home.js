//displaing poll data on table
$(document).ready(function () {
  $.ajax({
    url: 'http://127.0.0.1:8000/polls/',
    dataType: 'json',
    success: function (data) {
      count = 1;
      for (var i = 0; i < data.length; i++) {
        a = Object.values(data[i].OptionVote).reduce((a, b) => a + b, 0);
        //line 11 is creating [no, question-with blue line, total votes, tags]
        var row = $('<tr><td>' + count +
          '</td><td> ' + data[i].Question +
          //when line cliked call get elements by id API
          '<a href="http://127.0.0.1:8000/polls/'+data[i].id+'"> <hr class="lines" style="height:1px; width:50%;  background-color:blue; id="' + data[i].id + '""></hr></a>' +
          '</td><td>' + a +
          '</td><td>' + data[i].Tags +
          '<ts>');
        $('#myTable').append(row);
        count++;
      }

    }
  });
});

//displaying all tags 
$.get('http://127.0.0.1:8000/polls/tags/', function (data) {
  var no_tags = data.Tags.length;
  for (var i = 0; i < no_tags; i++) {
    tag_value = data.Tags[i];
    tag_view = '<input class="tagbox" type="checkbox"  value="' + tag_value + '"><label for="' + tag_value + '">' + tag_value + '</label><br></br>';
    filter_button = '<input type="button" id="Filter_by_tags" name="Filter_by_tags" value="Filter_by_tags"/>'
    $('#disptags').append(tag_view)
  }
  $('#disptags').append(filter_button)

  //storing checked values of checkbox
  $(function () {
    var checkedboxlist = [];
    $('#Filter_by_tags').click(function () {
      $(':checkbox:checked').each(function (i) {
        checkedboxlist[i] = $(this).val();
      });

      //GET tag data using query-string 
      $.ajax({
        url: 'http://127.0.0.1:8000/polls/?Tags=' + checkedboxlist,
        dataType: 'json',
        success: function (data) {
          count = 1;
          $('#myTable').empty();
          for (var i = 0; i < data.length; i++) {
            a = Object.values(data[i].OptionVote).reduce((a, b) => a + b, 0);
            var row = $('<tr><td>' + count + '</td><td>' + data[i].Question + '</td><td>' + a + '</td><td>' + data[i].Tags + '<ts>');
            $('#myTable').append(row);
            count++;
          }
        }
      });
    });
  });
});
