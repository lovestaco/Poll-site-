//add option button
function ad() {

    var option = '<input type="text" class="optionclass"  size="90px" ><br>';
    $('#optiondiv').append(option);
    console.log(option + " addOP");
    //var option = document.getElementById(count).value;

}
//send data- create poll
function myFunction() {
console.log("button clikecd");
    data_dict = {};
    var question = document.getElementById("questionname").value;
    var options = document.getElementsByClassName("optionclass");
    var tags = document.getElementById("tag").value;
    print(tags)
    data_dict = { "Question": question, "OptionVote": {}, "Tags": [tags] }
    for (var i = 0; i < options.length; i++) {
        data_dict["OptionVote"][options[i].value] = "0";
    }
    console.log(data_dict);


   $.ajax({
       url: 'http://127.0.0.1:8000/polls/',
        data: JSON.stringify(data_dict),
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',

    });
}