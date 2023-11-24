document.getElementById('loadData').addEventListener('click', function() {
    // Recuperar y descomprimir de localStorage
    var compressed_orders = localStorage.getItem('orders');
    var orders = JSON.parse(LZString.decompressFromUTF16(compressed_orders));

    // Enviar los datos al backend con una solicitud AJAX
    $.ajax({
        url: '/ruta/a/tu/endpoint',
        type: 'post',
        data: { 'orders': localStorage.getItem('orders') },
        success: function(response) {
            // Manejar respuesta
        }
    });
});
