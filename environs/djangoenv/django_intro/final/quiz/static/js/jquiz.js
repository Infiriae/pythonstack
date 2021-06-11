$(document).ready(function() {
    var slide = 1;
    var theme = 0;
    $.get("https://opentdb.com/api_category.php", function(res) {
        for (var i = 0; i < res.trivia_categories.length; i++) {
            $('#cat').append(
                '<option value="' +
                res.trivia_categories[i].id +
                '">' +
                res.trivia_categories[i].name +
                '</option>'
            );
        }
    });

    $('#cat').change(function() {});

    $('#go').click(function() {
        var cat = $('#cat').children('option:selected').text();
        if (theme === 1) {
            var color = "text-light";
        } else {
            var color = "";
        }
        if (cat === 'Mixed') {
            $('.quiztitle').html('<h3 class="' + color + '">Let\'s test your knowledge!</h3>');
        } else {
            $('.quiztitle').html('<h3 class="' + color + '">Let\'s see what you know about ' + cat + '</h3>');
        }

        var pick = $('#cat').val();
        $('#choosecat, label, #go').hide();
        $.get("https://opentdb.com/api.php?amount=10&category=" + pick, function(ress) {
            console.log(ress);
            for (var i = 0; i < ress.results.length; i++) {
                $('#jsonyou').append(
                    '<div class="row bg-image"><span id="img' + i + '"></span></div>'
                )
                $('#jsonfind').append(
                    '<div  id=' + i + ' class="row"><h3 class="font-weight-bold p-3 ' + color + '">' +
                    ress.results[i].question +
                    '</h3>'
                );
                var mod = [];
                if (ress.results[i].type === 'multiple') {
                    mod.push(ress.results[i].correct_answer);
                    for (var o = 0; o < ress.results[i].incorrect_answers.length; o++) {
                        mod.push(ress.results[i].incorrect_answers[o]);
                    }
                    var answ = (mod.length);
                    var nums = [];
                    for (var x = 1; x <= answ; x++) {
                        nums.push(x);
                    }
                    var rando = [];
                    var j = 0;
                    while (answ-- > 0) {
                        j = Math.floor(Math.random() * (answ + 1));
                        rando.push(nums[j]);
                        nums.splice(j, 1);
                    }
                    for (x = 0; x < rando.length; x++) {
                        $('#' + i).append(
                            '<p answer="' + ress.results[i].correct_answer + '" id="' + i + x + '" class="question ' + color + ' text-center p-3">' +
                            mod[rando[x] - 1] +
                            '</p>'
                        );
                    }
                } else {
                    $('#' + i).append(
                        '<p answer="' + ress.results[i].correct_answer + '"  id="' + i + 0 + '" class="question ' + color + ' text-center p-3">' +
                        'True' +
                        '</p>' +
                        '<p answer="' + ress.results[i].correct_answer + '"  id="' + i + 1 + '" class="question ' + color + ' text-center p-3">' +
                        'False' +
                        '</p>'
                    );
                }
            }
        });
    });

    $(document).on('click', '.question', function() {
        if (theme === 1) {
            var color = "text-light";
        } else {
            var color = "";
        }
        console.log($(this).text());
        if ($(this).text() === $(this).attr('answer')) {
            console.log('Correct!');
            $(this).removeClass('question');
            $(this).siblings().removeClass('question');
            $(this).addClass('bg-success');
            $('#img' + $(this).parent().attr('id')).html('<img style="height: 35vh;" src="img/yes.png" alt="Correct!">');
            $('#img' + $(this).parent().attr('id')).append('<p class="' + color + '">Yes! The answer was ' + $(this).attr('answer') + '!</p>');
        } else {
            $(this).removeClass('question');
            $(this).siblings().removeClass('question');
            $(this).addClass('bg-danger');
            $('#img' + $(this).parent().attr('id')).html('<img style="height: 35vh;" src="img/no.png" alt="Wrong!">');
            $('#img' + $(this).parent().attr('id')).append('<p class="' + color + '">Actually, the answer was ' + $(this).attr('answer') + '!</p>');
            console.log('Wrong!');
        }
    });


    $('#login').submit(function() {
        var i = ($("input").first().val());
        $('#picture').html('<h1>' + i + '</h1>');
    });

    $('#you').click(function() {
        $('#Uname').text('Name?');
    });

    $('#show1').click(function() {
        location.reload();
    });

    $('#show2').click(function() {
        // $('#pushitout').slideToggle();
        if (slide === 0) {
            slide = 1;
            console.log(mod);
            $('#pushitout').hide('');
            $('#pushitout2').fadeOut('');
        } else {
            slide = 0;
            $('#pushitout').show('');
            $('#pushitout2').fadeIn('');
        }
    });

    $('#theme').click(function() {
        if (theme === 0) {
            theme = 1;
            $('#theme').text('No change it back.');
            $('p, h1, h3, label').addClass('text-light');
            $('body').removeClass('bg-info');
            $('body').addClass('bg-dark');
        } else {
            theme = 0;
            $('#theme').text('Nevermind. I like it dark.');
            $('p, h1, h3, label').removeClass('text-light');
            $('body').removeClass('bg-dark');
            $('body').addClass('bg-info');
        }
    });
});