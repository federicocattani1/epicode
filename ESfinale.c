#include <stdio.h>
#include <string.h>

int main() {
    int punti = 0, nuovapartita = 1, rg = 0;
    char partita = '0', r1 = '0', r2 = '0', r3 = '0';
    char nome[11];
    
    while (nuovapartita == 1) {
        printf("Giochiamo? (inserire a o b)\n");
        scanf(" %c", &partita);

        if (partita == 'a') {
            printf("Inserisci il tuo nome: ");
            scanf("%s", nome);
            while(strlen(nome)>10){
                            printf("nome troppo lungo, inserirne uno piu corto\n");
                            printf("Inserisci il tuo nome: ");
                            scanf("%s", nome);
                        }
            do {
                printf("Quale di questi non è un linguaggio di programmazione? (inserire la lettera corrispondente)\n"
                       "a) c++\n"
                       "b) udp\n"
                       "c) python\n");
                scanf(" %c", &r1);
                if(r1 != 'a' && r1 != 'b' && r1 != 'c'){
                    printf("selezione non valida, riprovare\n");
                }
            } while (r1 != 'a' && r1 != 'b' && r1 != 'c');
            
            if (r1 == 'b') {
                punti++;
                printf("risposta corretta\n");
            } 
            else {
                printf("risposta sbagliata\n");
            }
            
            do {
                printf("Quale di questi è un messaggio di errore nel protocollo http?\n"
                       "a) 200\n"
                       "b) 301\n"
                       "c) 404\n");
                scanf(" %c", &r2);
                if(r2 != 'a' && r2 != 'b' && r2 != 'c'){
                    printf("selezione non valida, riprovare\n");
                }
            } while (r2 != 'a' && r2 != 'b' && r2 != 'c');
            
            if (r2 == 'c') {
                punti++;
                printf("risposta corretta\n");
            } 
            else {
                printf("risposta sbagliata\n");
            }
            
            do {
                printf("Da quanti bit è composto un byte?\n"
                       "a) 4\n"
                       "b) 16\n"
                       "c) 8\n");
                scanf(" %c", &r3);
                if(r3 != 'a' && r3 != 'b' && r3 != 'c'){
                    printf("selezione non valida, riprovare\n");
                }
            } while (r3 != 'a' && r3 != 'b' && r3 != 'c');
            
            if (r3 == 'c') {
                punti++;
                printf("risposta corretta\n");
            } 
            else {
                printf("risposta sbagliata\n");
            }

            printf("%s hai totalizzato un punteggio di %d/3\n", nome, punti);
            
        }
        else if (partita == 'b') {
            printf("Arrivederci!\n");
            nuovapartita = 0;
        }
        else {
            printf("Selezione non valida, riprovare.\n");
        }
    }

    return 0;
}

