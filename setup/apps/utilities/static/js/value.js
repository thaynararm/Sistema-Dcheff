$(document).ready(function(){
    $('.value').mask('000.000.000.000.000,00', {reverse: true});
    $('.value').on('input', function(e){
        var value = $(this).val().replace(/\D/g, '');

        if(value.length > 2){
            // Remove os zeros à esquerda
            value = value.replace(/^0+/, '');

            // Adiciona a vírgula e os centavos
            var cents = value.slice(-2);
            var integerPart = value.slice(0, -2) || '0';

            // Adiciona os pontos para separar as milhas
            var formattedValue = '';
            for (var i = integerPart.length; i > 0; i -= 3) {
                formattedValue = '.' + integerPart.slice(Math.max(0, i - 3), i) + formattedValue;
            }
            formattedValue = formattedValue.slice(1); // Remove o ponto inicial, se houver

            $(this).val(formattedValue + ',' + cents);
        } else if(value.length === 2){
            // Adiciona '0,' seguido dos centavos
            $(this).val('0,' + value);
        } else if(value.length === 1){
            // Adiciona '0,0' seguido do valor digitado
            $(this).val('0,0' + value);
        }
    });
});
