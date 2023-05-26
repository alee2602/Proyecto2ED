



# to open/create a new html file in the write mode
f = open('index.html', 'w')

# the html code which will go in the file index.html
html_template = """<html>
<!DOCTYPE html>
<html>
<head>
    <title>Moodtify</title>
    <style>
        body {
            background-image: url('Fondo.jpeg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            position: relative;
            color: #fff;
            font-family: 'Arial', sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        
        .overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            pointer-events: none;
        }
        
        .header {
            background-color: #194016;
            padding: 15px;
            text-align: left;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            height: 80px;
        }
        
        .header h1 {
            margin: 0;
        }
        
        .header .buttons-container {
            display: flex;
            flex-direction: row;
            justify-content: flex-start;
            align-items: center;
            margin-top: 10px;
        }
        
        .header .buttons-container .tab {
            background-color: #000;
            color: #fff;
            font-family: 'Toolify', sans-serif;
            border: none;
            border-radius: 20px;
            padding: 10px 20px;
            margin-right: 10px;
            cursor: pointer;
        }
        
        .header .buttons-container .dropdown {
            position: relative;
            display: inline-block;
            margin-right: 10px;
        }
        
        .header .buttons-container .dropdown .tab {
            padding-right: 25px;
        }
        
        .header .buttons-container .dropdown .dropdown-content {
            display: none;
            position: absolute;
            background-color: #99ff99;
            min-width: 120px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
        }
        
        .header .buttons-container .dropdown .dropdown-content p {
            color: #000;
            padding: 8px 12px;
            margin: 0;
            cursor: pointer;
        }
        
        .header .buttons-container .dropdown:hover .dropdown-content {
            display: block;
        }
        
        .content {
            margin-top: 180px;
        }
        
        .content .input-group {
            margin-top: 30px;
        }
        
        .content h3 {
            font-size: 28px;
            margin-top: -20px;
        }
        
        .content input[type="text"] {
            padding: 15px;
            border-radius: 20px;
            border: none;
            width: 400px;
        }
        
        .content button {
            background-color: #000;
            color: #fff;
            font-family: 'Toolify', sans-serif;
            border: none;
            border-radius: 20px;
            padding: 10px 20px;
            margin-top: 20px;
            cursor: pointer;
        }
        
        .footer {
            background-color: #194016;
            padding: 15px;
            text-align: center;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80px;
        }
        
        .footer p {
            margin: 0;
        }
        
        .footer img {
            width: 20px;
            vertical-align: middle;
            margin-right: 5px;
        }
        
        .date {
            position: absolute;
            top: 15px;
            right: 15px;
        }
    </style>
</head>
<body>
    <div class="overlay"></div>
    <div class="header">
        <h1>Moodtify</h1>
        <img src="logo.png" style="width: 75px;position: absolute;left: 150px;top: 15px;" alt="">
        <br>
        <div class="buttons-container">
            <button class="tab" onclick="showGenreQuestion()">Elección de género</button>
            <button class="tab" onclick="showMoodQuestion()">Estado de Animo</button>
            <div class="dropdown">
                <button class="tab dropdown-button">Idioma &#9660;</button>
                <div class="dropdown-content">
                    <p>Español</p>
                    <p>Inglés</p>
                    <p>Portugués</p>
                    <p>Coreano</p>
                </div>
            </div>
            <button class="tab">Login</button>
        </div>
    </div>
    
    <div class="content">
        <div class="input-group">
            <h3>¿Qué género musical te gustaría escuchar ahora?</h3>
            <input type="text" placeholder="Escribe aquí">
            <button onclick="search()">Buscar</button>
        </div>
    </div>
    
    <div class="footer">
        <p><img src="gmail.png"> Contactanos en Gmail | <img src="phone.png"> Contactanos por teléfono | <img src="instagram.png"> Contactanos en Instagram | <img src="twitter.png"> Contactanos en Twitter</p>
    </div>
    
    <div class="date">
        <p>Fecha: <span id="current-date"></span></p>
    </div>
    
    <script>
        const currentDate = new Date();
        document.getElementById('current-date').innerText = currentDate.toLocaleDateString();
        
        function showMoodQuestion() {
            const content = document.querySelector('.content');
            content.innerHTML = `
                <div class="input-group">
                    <h3>¿A qué estado de ánimo quieres llegar hoy?</h3>
                    <input type="text" placeholder="Escribe aquí">
                    <button onclick="search()">Buscar</button>
                </div>
            `;
        }
        
        function showGenreQuestion() {
            const content = document.querySelector('.content');
            content.innerHTML = `
                <div class="input-group">
                    <h3>¿Qué género musical te gustaría escuchar ahora?</h3>
                    <input type="text" placeholder="Escribe aquí">
                    <button onclick="search()">Buscar</button>
                </div>
            `;
        }
        
        function search() {
            const searchTerm = document.querySelector('input[type="text"]').value;
            // Realizar la búsqueda con el término ingresado
            console.log('Búsqueda:', searchTerm);
        }
    </script>
</body>
</html>
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()

# import module
import codecs

# to open/create a new html file in the write mode
f = open('GFG.html', 'w')

# the html code which will go in the file GFG.html
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Moodtify</title>
    <style>
        body {
            background-image: url('Fondo.jpeg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            position: relative;
            color: #fff;
            font-family: 'Arial', sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        
        .overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            pointer-events: none;
        }
        
        .header {
            background-color: #194016;
            padding: 15px;
            text-align: left;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            height: 80px;
        }
        
        .header h1 {
            margin: 0;
        }
        
        .header .buttons-container {
            display: flex;
            flex-direction: row;
            justify-content: flex-start;
            align-items: center;
            margin-top: 10px;
        }
        
        .header .buttons-container .tab {
            background-color: #000;
            color: #fff;
            font-family: 'Toolify', sans-serif;
            border: none;
            border-radius: 20px;
            padding: 10px 20px;
            margin-right: 10px;
            cursor: pointer;
        }
        
        .header .buttons-container .dropdown {
            position: relative;
            display: inline-block;
            margin-right: 10px;
        }
        
        .header .buttons-container .dropdown .tab {
            padding-right: 25px;
        }
        
        .header .buttons-container .dropdown .dropdown-content {
            display: none;
            position: absolute;
            background-color: #99ff99;
            min-width: 120px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
        }
        
        .header .buttons-container .dropdown .dropdown-content p {
            color: #000;
            padding: 8px 12px;
            margin: 0;
            cursor: pointer;
        }
        
        .header .buttons-container .dropdown:hover .dropdown-content {
            display: block;
        }
        
        .content {
            margin-top: 180px;
        }
        
        .content .input-group {
            margin-top: 30px;
        }
        
        .content h3 {
            font-size: 28px;
            margin-top: -20px;
        }
        
        .content input[type="text"] {
            padding: 15px;
            border-radius: 20px;
            border: none;
            width: 400px;
        }
        
        .content button {
            background-color: #000;
            color: #fff;
            font-family: 'Toolify', sans-serif;
            border: none;
            border-radius: 20px;
            padding: 10px 20px;
            margin-top: 20px;
            cursor: pointer;
        }
        
        .footer {
            background-color: #194016;
            padding: 15px;
            text-align: center;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80px;
        }
        
        .footer p {
            margin: 0;
        }
        
        .footer img {
            width: 20px;
            vertical-align: middle;
            margin-right: 5px;
        }
        
        .date {
            position: absolute;
            top: 15px;
            right: 15px;
        }
    </style>
</head>
<body>
    <div class="overlay"></div>
    <div class="header">
        <h1>Moodtify</h1>
        <img src="logo.png" style="width: 75px;position: absolute;left: 150px;top: 15px;" alt="">
        <br>
        <div class="buttons-container">
            <button class="tab" onclick="showGenreQuestion()">Elección de género</button>
            <button class="tab" onclick="showMoodQuestion()">Estado de Animo</button>
            <div class="dropdown">
                <button class="tab dropdown-button">Idioma &#9660;</button>
                <div class="dropdown-content">
                    <p>Español</p>
                    <p>Inglés</p>
                    <p>Portugués</p>
                    <p>Coreano</p>
                </div>
            </div>
            <button class="tab">Login</button>
        </div>
    </div>
    
    <div class="content">
        <div class="input-group">
            <h3>¿Qué género musical te gustaría escuchar ahora?</h3>
            <input type="text" placeholder="Escribe aquí">
            <button onclick="search()">Buscar</button>
        </div>
    </div>
    
    <div class="footer">
        <p><img src="gmail.png"> Contactanos en Gmail | <img src="phone.png"> Contactanos por teléfono | <img src="instagram.png"> Contactanos en Instagram | <img src="twitter.png"> Contactanos en Twitter</p>
    </div>
    
    <div class="date">
        <p>Fecha: <span id="current-date"></span></p>
    </div>
    
    <script>
        const currentDate = new Date();
        document.getElementById('current-date').innerText = currentDate.toLocaleDateString();
        
        function showMoodQuestion() {
            const content = document.querySelector('.content');
            content.innerHTML = `
                <div class="input-group">
                    <h3>¿A qué estado de ánimo quieres llegar hoy?</h3>
                    <input type="text" placeholder="Escribe aquí">
                    <button onclick="search()">Buscar</button>
                </div>
            `;
        }
        
        function showGenreQuestion() {
            const content = document.querySelector('.content');
            content.innerHTML = `
                <div class="input-group">
                    <h3>¿Qué género musical te gustaría escuchar ahora?</h3>
                    <input type="text" placeholder="Escribe aquí">
                    <button onclick="search()">Buscar</button>
                </div>
            `;
        }
        
        function search() {
            const searchTerm = document.querySelector('input[type="text"]').value;
            // Realizar la búsqueda con el término ingresado
            console.log('Búsqueda:', searchTerm);
        }
    </script>
</body>
</html>
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()

# viewing html files
# below code creates a
# codecs.StreamReaderWriter object
file = codecs.open("index.html")

# using .read method to view the html
# code from our object
print(file.read())

# import module
import webbrowser

# open html file
webbrowser.open('index.html')

# import module