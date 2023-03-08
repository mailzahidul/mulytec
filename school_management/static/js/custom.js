
$(".js-create-product").click(function () {
    $.ajax({
      url: 'products-create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-product").modal("show");
      },
      success: function (data) {
        $("#modal-product .modal-content").html(data.html_form);
      }
    });
  });




function multiple_img_remove(product_id, img_id){
    if(confirm("Do you really want to delete this image?")){
        $.ajax({
            type: 'get',
            url: '/admin/img-delete/',
            data: {
            'product_id':product_id,
            'img_id':img_id
              },
            success:function(data){
                $('#multiple_img_show').html('');
                $('#multiple_img_show').append(data.data);


            },
            error: function(ts) { alert(ts.responseText) }
        });
    }
}
