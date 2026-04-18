from transliterate import translit
from num2words import num2words

print(translit("Ladies and gentlemen, I'm " 
	+ num2words(78) + " years old and I finally got "
	+ num2words(15) + " minutes of fame once in a lifetime and I guess that this is mine. People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.", 'ru'));
print("");
print(translit("More than " 
	+ num2words(3) + " years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last "
	+ num2words(40) + ". When I was "
	+ num2words(8) + "...", 'ru')); 