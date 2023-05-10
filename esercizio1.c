#include <stdio.h>
#include <string.h>

int main (){
int punti=0, nuovapartita=1;
char partita [10], nome[50], r1[10], r2[10], r3[10];
while (nuovapartita == 1){
printf("Giochiamo? (inserire si o no)\n");
scanf("%s", partita);
if(strcmp(partita, "si") == 0) {
printf("Inserisci il tuo nome: ");
scanf("%s", nome);
printf("Quale di questi non e' un linguaggio di programmazione? (inserire la lettera corrispondente)\na)c++\nb)udp\nc)python\n");
scanf("%s", r1);
if (strcmp(r1, "b") == 0) {
punti++;
printf("risposta corretta\n");
}
else {
printf("risposta sbagliata\n");
}
printf("Quale di questi e' un messaggio di errore nel protocollo http?\na)200\nb)301\nc)404\n");
scanf("%s", r2);
if (strcmp(r2, "c") == 0) {
punti++;
printf("risposta corretta\n");
}
else {
printf("risposta sbagliata\n");
}
printf("Da quanti bit e' composto un byte?\na)4\nb)16\nc)8\n");
scanf("%s", r3);
if (strcmp(r3, "c") == 0) {
punti++;
printf("risposta corretta\n");
}
else {
printf("risposta sbagliata\n");
}

printf("%s hai totalizzato un punteggio di %d/3\n", nome, punti);
}
else{
printf("Arrivederci!\n");
nuovapartita=0;
}
}


return 0;
}






