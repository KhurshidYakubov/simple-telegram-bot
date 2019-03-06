
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Tg-bot</title>
</head>
<body>
<form method="post">
    <textarea name="sometext"  cols="30" rows="10"></textarea>
    <button type="submit">Send</button>
</form>

</body>
</html>



<?php

  $token = "679237768:AAHepOdmExd31NekARs6TJdQNmp6PASgmsE";

  $user_id = 479794394;
    if (isset($_POST["sometext"])) {
        $mesg = $_POST["sometext"];
        $request_params =[
            'chat_id' => $user_id,
            'text' => $mesg
        ];


        $request_url = 'https://api.telegram.org/bot' . $token . '/sendMessage?' . http_build_query($request_params);
        file_get_contents($request_url);

    }
?>

