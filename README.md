# Quantum-encryption
this is a new way of encrypting data using qubits.
in this program the qubits are simulated using qiskit.
<h1 style="color: red">attention</h1>
<li>the more you increase shots the more the program is accurate but do not increase a lot or you are going to kill your laptop</li>
<li>you cannot put strings with more than 28 characters due to limited resources from qiskit</li>

## The idea
the program takes a message <i>M</i> and turns it into [<i>m<sub>1</sub>, m<sub>2</sub>, ... </i>] which is then turned into its ACSII values [<i>A<sub>1</sub>, A<sub>2</sub>, ...</i>]/256 so it is between 0 and 1
after that it sends qubits each like |<i>q<sub>i</sub></i>⟩ = <i>cos((&pi; / 2) * A<sub>i</sub></i>)</i>|0⟩ + <i>sin((&pi; / 2) * A<sub>i</sub></i>)</i>|1⟩
and then on measurement the result collapses into 0s and 1s many times, we count how many 0s were there divide them by the number of samples and then we get an approximate of the polirization of the qubits and reverse the equation to get M again

# How to Contribute
1. Fork the Repository
Click the Fork button on the top-right of the repository page.
Clone your forked repository:
git clone https://github.com/your-username/Quantum-encryption.git
Navigate into the project directory:
cd Quantum-encryption
Add the original repository as a remote:
git remote add upstream https://github.com/KevinityAlwaysCamelCase/Quantum-encryption.git
2. Create a Branch
Before making changes, create a new branch:
git checkout -b feature-name
3. Make Your Changes
Improve the encryption or decryption algorithm.
Optimize performance or increase accuracy.
Add tests or improve documentation.
Fix bugs or report issues.
4. Commit and Push
Stage your changes:
git add .
Commit with a meaningful message:
git commit -m "message here(don't write something too big)"
Push to your forked repository:
git push origin feature-name
5. Create a Pull Request (PR)
Go to the original repository on GitHub.
Click on the Pull Requests tab.
Click New Pull Request.
Select your branch and describe the changes.
Submit the PR for review.
## Reporting Issues
If you find a bug or have suggestions, open an issue:
Click on the Issues tab.
Click New Issue.
Describe the problem or feature request.
## Coding Guidelines
Write meaningful commit messages.
Keep functions modular and well-documented.
