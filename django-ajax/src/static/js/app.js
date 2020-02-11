$(document).ready(function(){

    $.ajax({
    url:  'room_main',
    type:  'get',
    data:{
        
    }
    success: function  (data) {
       
    
    });
})

    $('[#myTable](https://paper.dropbox.com/?q=%23myTable) > tbody').append(rows);
    $('.deleteBtn').each((i, elm) => {
        $(elm).on("click",  (e) => {
            deleteRoom($(elm))
        })
    })
    }
});

function  deleteRoom(el){
    roomId  =  $(el).data('id')
    $.ajax({
        url:  `/rooms/delete/${roomId}`,
        type:  'post',
        dataType:  'json',
        success:  function (data) {
            $(el).parents()[1].remove()
        }
    });
}