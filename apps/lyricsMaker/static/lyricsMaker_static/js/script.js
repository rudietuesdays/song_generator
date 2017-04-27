function getBey(res){
    var images = " ";
    // for(var i = 0; i < res.images.length; i++) {
        // images+="<img src='"+res.images[i].url+"' alt=>";
        // }
    images = "<img src='"+res.album.images[0].url+"' alt=>"
}

function beyMood(res){

    var mood = $('#mood').val()
    song = ''

    if (mood == 'happy'){
        song = '3axkNosdVQLZiq1HakuGhc'
    }
    if (mood == 'dancey'){
        song = '02M6vucOvmRfMxTXDUwRXu'
    }
    if (mood == 'sad'){
        song = '31acMiV67UgKn1ScFChFxo'
    }
    if (mood == 'vengeful'){
        song = '2ZBNclC5wm4GtiWaeh0DMx'
    }
    if (mood == 'loving'){
        song = '5IVuqXILoxVWvWEPm82Jxr'
    }
    $.get(("https://api.spotify.com/v1/tracks/"+song), function(res){
        $('.player').html(
            `<iframe src="https://embed.spotify.com/?uri=spotify:track:${song}" frameborder="0" allowtransparency="true"></iframe>`
        )
        beyBackground(res)
    })
}

function beyBackground(res){
    images = res.album.images[0].url
    $('#wrapper').css(
        "background", "url("+ images + ") no-repeat"
    ).css("background-size", "cover");
}

$(document).ready(function(){
    console.log('working');

    $('.bey_moods').submit(function(e){
        e.preventDefault();
        console.log('Mood selection is: '+$('#mood').val());
        beyMood()
    })

    // $('.building_blocks').submit(function(e){
    //     e.preventDefault();
        // $.ajax({
        //     url: "/",
        //     method: 'post',
        //     data: $(this).serialize(),
        //     success: function(serverResponse){
        //         $('.notes').html(serverResponse)
        //         console.log("Received this from server: ", serverResponse)
        //     },
        // })
    // })

    // $('h2').on('click', function(){
    //     $.get('https://api.spotify.com/v1/tracks/31acMiV67UgKn1ScFChFxo', function(res){
    //         console.log(res);
    //         getBey(res);
    //     })
    // })

})
