# Teus Game

<p align="justify">Main project for the one-week intensive undergrad course "<b>Computational Tools: The Art of Programming</b>", which delves mainly into <i>game development</i> fundamentals including object-oriented programming patterns, event handling, sprite animation, collision detection, game mechanics implementation, user interface design, player engagement strategies, game physics, and playtesting methodologies.</p>

<p align="justify">This game is a free recreation of the popular <b>T-Rex Dinosaur Game</b>, which appears when there is no internet connection while performing searches in Google Chrome. In particular, it is based on the implementation by the user <i>maxontech</i>, created in <b>Python</b> and using the <i>Pygame</i> library for 2D video game development. Below is the link to the base project repository: </p> 

[maxontech/chrome-dinosaur](https://github.com/maxontech/chrome-dinosaur)

<p align="center">
  <img src="https://github.com/user-attachments/assets/3f3575f0-eab2-40e0-8b84-6891a361c684" alt = "Teus"/>
</p>

## Key Differences

<p align="justify">The first noticeable difference is in the graphics. The T-Rex character is replaced by <b>Teus</b>, the mascot of the Tecnológico de Monterrey. The desert background changes to the iconic landscape of the Monterrey campus rector’s office. The cacti, which represent obstacles, are now modeled as animals (deer, peacock, and cat) that roam around the campus.</p> 

<p align="center">
  <img src="https://github.com/user-attachments/assets/605179e4-668a-4fdf-a064-25c7146c9970" alt = "Gameplay"/>
</p>

## How to Execute (Windows Only)

1. **Install Python**:

<p align="justify">Make sure you have Python installed on your system. You can download it from the official website: <a href="https://www.python.org/downloads/">Python Downloads</a>. Ensure you add Python to your system's PATH during installation.</p>

2. **Install Pygame**:

<p align="justify">To install Pygame, open your command prompt and run the following command:</p>

```bash
pip install pygame
```

3. **Download the Game Files**:

<p align="justify">Clone or download the repository to your local machine. If using Git, you can run:</p>

```bash
git clone https://github.com/fectec/TeusGame.git
```
4. **Run the Game**:

<p align="justify">Open a command prompt in the directory where the game files are located. Execute the game by running:</p>

```bash
python main.py
```
<p align="justify">The game should now launch in a new window. Enjoy playing Teus Game!</p>

## Gameplay Mechanics

<p align="justify">Mechanically, the game offers a very similar experience to the original. However, to enrich the gameplay and prevent monotony, a classic power-up has been added: the <b>invincibility shield</b>. This provides extra fun for players.</p> 

<p align="justify">Additionally, several elements were included to improve user satisfaction, such as a score menu, background music, and sound effects. Finally, the hitboxes (collision boxes) for the enemies were improved, making it more intuitive for players when they hit obstacles and lose the game.</p> 

<p align="center">
  <img src="https://github.com/user-attachments/assets/d32a1a1b-1137-4c45-a5bd-9b4cfa074a8e" alt = "Shield"/>
</p>

## Development Team & Timeline

<p align="justify">This project was developed by programmers Juan (<a href="https://github.com/fectec">github.com/fectec</a>) and Joirid (<a href="https://github.com/Joirid">github.com/Joirid</a>). Juan designed the Protagonist, Enemy, and Obstacle classes, which implement the respective entity functionalities. Joirid focused on the Item and Shield classes, programming the unique shield feature for Teus Game.</p> 

<p align="justify">The project began on Monday with an analysis of various games we had tried, as well as exploring base codes to expand the game. One of the most promising was the T-Rex Dinosaur Game, which ultimately became the foundation for the final game.</p> 

<p align="justify">After selecting the base game, we identified potential improvements for the new version (theme it around the university, change protagonist, environment, and obstacles, and include a shield to protect the player for a limited time).</p>
  
<p align="justify">On Tuesday, we delved deeper into the code, starting to work on the main character and its movements, though without any changes for the final project.</p>

<p align="justify">By Wednesday, progress had been made in modifying the protagonist, environment, and obstacles—Teus replaced the dinosaur, the desert background was replaced by the rector’s office, and the cacti were replaced by campus animals. Music was also added to enhance the experience.</p> 

<p align="justify">Thursday focused on the shield item’s functionality and improving collision detection between the protagonist and obstacles.</p>
  
<p align="justify">On Friday, we completed the development of the menu and fine-tuned the shield feature.</p> 

<p align="center">
  <img src="https://github.com/user-attachments/assets/4c24f3d9-7f4a-4bce-931b-50adab2184a3" alt = "Peacock"/>
</p>

## Conclusions

<p align="justify">The outcome of this project reinforces the importance of balancing <i>usability</i> and gameplay when developing video games. It ensures that players are motivated to continue playing, without making the game either too monotonous or too difficult. Furthermore, throughout this week, we gained valuable insight into game development in Python and learned about useful libraries to assist in creating such programs.</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/27180b5d-dae7-47dd-9c27-435a4de9d6de" alt = "Cat"/>
</p>
