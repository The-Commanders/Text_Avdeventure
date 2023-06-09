import pytest
import random
from rich.console import Console
from rich.prompt import Prompt
from adventure.environments.ruins_entrance import RuinsEntrance
from adventure.confirm_evironment import confirm_environment

console = Console()


def test_ruins_entrance_exists():

    ruins_entrance = RuinsEntrance(console.print, Prompt.ask)

    assert ruins_entrance


def test_ruins_ent_event_one_c1():
    expected_text = """
 [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    It seems like the door to get into the ruins is closed and you don't have the key. How would you like
    to proceed in order to gain access to the ruins?
    1. Climb the wall using your grappling hook.
    2. Try and pick the lock.
    3. Try and find the key somewhere around.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:
: 1
You do not have a grappling hook!
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:
: 2
[#FFA500]
    Did you really think you would be able to pick the lock? You've made a great effort but accomplished nothing.
    """

    sim_choice = ["1", "2"]

    confirm_environment(RuinsEntrance, "event_one", expected_text, sim_choice)


def test_ruins_ent_event_one_c2():
    expected_text = """
 [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    It seems like the door to get into the ruins is closed and you don't have the key. How would you like
    to proceed in order to gain access to the ruins?
    1. Climb the wall using your grappling hook.
    2. Try and pick the lock.
    3. Try and find the key somewhere around.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:
: 2
[#FFA500]
    Did you really think you would be able to pick the lock? You've made a great effort but accomplished nothing.
        """

    sim_choice = ["2"]

    confirm_environment(RuinsEntrance, "event_one", expected_text, sim_choice)


def test_ruins_ent_event_one_c3():
    expected_text = """
  [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    It seems like the door to get into the ruins is closed and you don't have the key. How would you like
    to proceed in order to gain access to the ruins?
    1. Climb the wall using your grappling hook.
    2. Try and pick the lock.
    3. Try and find the key somewhere around.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:
: 3
[#FFA500]
    That was a long and unsuccessful walk. The key is nowhere to be found, just like your energy.
        """

    sim_choice = ["3"]

    confirm_environment(RuinsEntrance, "event_one", expected_text, sim_choice)


def test_ruins_ent_event_two_c1():
    expected_text = """
[#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    As you jump into the ruins, you find yourself surrounded by scorpions. 
        What do you do?
    "1. Try to kill them with your survival knife.
    "2. Run as fast as you can into the ruins so they don't catch you.
    "3. Climb the wall back out.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:  
    : 1
[#FFA500]You do not have a survival knife!
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:  
    : 3
[#FFA500]
    You have fallen down the wall trying to climb back up and have hurt yourself.
     """

    sim_choice = ["1", "3"]

    confirm_environment(RuinsEntrance, "event_two", expected_text, sim_choice)


def test_ruins_ent_event_two_c2():
    expected_text = """
 [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    As you jump into the ruins, you find yourself surrounded by scorpions. 
        What do you do?
    "1. Try to kill them with your survival knife.
    "2. Run as fast as you can into the ruins so they don't catch you.
    "3. Climb the wall back out.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:  
    : 2
[#FFA500]
    You are one fast runner! You've made it without loosing any health.

     """

    sim_choice = ["2"]

    confirm_environment(RuinsEntrance, "event_two", expected_text, sim_choice)


def test_ruins_ent_event_two_c3():
    expected_text = """
 [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    As you jump into the ruins, you find yourself surrounded by scorpions. 
        What do you do?
    "1. Try to kill them with your survival knife.
    "2. Run as fast as you can into the ruins so they don't catch you.
    "3. Climb the wall back out.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:  
    : 3
[#FFA500]
    You have fallen down the wall trying to climb back up and have hurt yourself.
         """

    sim_choice = ["3"]

    confirm_environment(RuinsEntrance, "event_two", expected_text, sim_choice)


def test_ruins_ent_event_three_c1_correct():
    expected_text = """
 [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    We now know you posses great strength and speed. But what about your wit?
    Complete one of the following challenges to get to the next level.
    1. Solve the riddle
    2. Word association.
    3. Unscramble the word.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:  
    : 1
    [#FFA500]I’m tall when I’m young, and I’m short when I’m old.
[#FFA500]
    What am I? Enter your answer:
    : candle
    [green]Correct[/green]! You've recovered some [red]health[/red] and [yellow]stamina[/yellow]

             """

    sim_choice = ["1", "candle"]

    confirm_environment(RuinsEntrance, "event_three", expected_text, sim_choice)


def test_ruins_ent_event_three_c1_incorrect():
    expected_text = """
  [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    We now know you posses great strength and speed. But what about your wit?
    Complete one of the following challenges to get to the next level.
    1. Solve the riddle
    2. Word association.
    3. Unscramble the word.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:  
    : 1
    [#FFA500]I’m tall when I’m young, and I’m short when I’m old.
[#FFA500]
        What am I? Enter your answer:
        : candl
    [red]Incorrect.    [#FFA500]I’m tall when I’m young, and I’m short when I’m old.
[#FFA500]
        What am I? Enter your answer:
        : candle
    [green]Correct[/green]! You've recovered some [red]health[/red] and [yellow]stamina[/yellow]
             """

    sim_choice = ["1", "candl", "candle"]

    confirm_environment(RuinsEntrance, "event_three", expected_text, sim_choice)


def test_ruins_ent_event_three_c3_correct():
    expected_text = """
 [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    We now know you posses great strength and speed. But what about your wit?
    Complete one of the following challenges to get to the next level.
    1. Solve the riddle
    2. Word association.
    3. Unscramble the word.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:  
    : 3
[#FFA500]
    Unscramble the word: TNVMERONG
    
[#FFA500]
    Enter your answer: 
    : government
    [green]Correct!
             """

    sim_choice = ["3", "government"]



    confirm_environment(RuinsEntrance, "event_three", expected_text, sim_choice)


def test_ruins_ent_event_three_c3_incorrect():
    expected_text = """
 [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    We now know you posses great strength and speed. But what about your wit?
    Complete one of the following challenges to get to the next level.
    1. Solve the riddle
    2. Word association.
    3. Unscramble the word.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:  
    : 3
[#FFA500]
    Unscramble the word: TNVMERONG
    
[#FFA500]
    Enter your answer: 
    : goverment
[#FFA500]
    [red]Incorrect[/red]. Looks like your unlucky this time..
    [#FFA500]
    Unscramble the word: TNVMERONG
    
[#FFA500]
    Enter your answer: 
    : government
    [green]Correct!
             """

    incorrect = "goverment"
    correct = "government"
    sim_choice = ["3", incorrect, correct]

    confirm_environment(RuinsEntrance, "event_three", expected_text, sim_choice)