 $(document).ready(function () {

        $.ajax({
            url: "/api/getComments/"+post_id,
            cache: false,
            success: function (data) {
                jQuery.each(data, function (index, item) {
                    build_comnments(item)
                })

            }
        });
    })
    function build_comnments(data) {
        $("#comment_section").append('  <div class="card shadow-0 border comments-background mb-2" >' +
            '<div class="card-body p-4">' +
            '<div class="card mb-4">' +
            '<div class="card-body">' +
            '<p>'+data.body+'</p>' +
            '<div class="d-flex justify-content-between">' +
            '<div class="d-flex flex-row align-items-center">' +
            '<div class="row"><div class="col-md-12"> '+data.name+'</div>'+
            '<div  class="small mb-0 ms-2"> <div class="col-md-12 ml-3">'+data.email+'</div> </div></div>' +
            '</div>' +
            '</div>' +
            '</div>' +
            '</div>' +
            '</div>' +
            '</div>');
    }
