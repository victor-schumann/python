#include <stdio.h>
#include <string.h>
#include "funcoesGenericas.h"


tipoData lerData(char msg[])
{
    tipoData data;
    int controlo;

    do
    {
        printf("%s", msg);
        controlo = scanf("%d-%d-%d", &data.dia, &data.mes, &data.ano);
        limparBuffer();

        if (controlo != 3)
        {
            printf("\nERRO: Formato de data invalido\n");
        }
    }
    while (controlo != 3);

    return data;
}

void escreverData(tipoData data)
{
    printf("%02d-%02d-%d", data.dia, data.mes, data.ano);
}

float lerFloat (char msg[], float limMin, float limMax)
{
    float num;
    int controlo;

    do
    {
        printf("%s", msg);
        controlo = scanf("%f", &num);
        limparBuffer();

        if (num < limMin || num > limMax || controlo == 0)
        {
            printf("\nERRO: o valor nao pertence ao intervalo [%.2f, %.2f]", limMin, limMax);
        }
    }
    while (num < limMin || num > limMax || controlo == 0);
    return num;
}


int lerInteiro (char msg[], int limMin, int limMax)
{
    int num, controlo;

    do
    {
        printf("%s[%d, %d]:", msg, limMin, limMax);
        controlo = scanf("%d", &num);
        limparBuffer();

        if (num < limMin || num > limMax || controlo == 0)
        {
            printf("\nERRO: o valor nao pertence ao intervalo [%d, %d]", limMin, limMax);
        }
    }
    while (num < limMin || num > limMax || controlo == 0);
    return num;
}


void lerString (char msg[], char texto[], int tamMax)
{
    int tamString;

    do
    {
        printf("%s", msg);
        fgets(texto, tamMax, stdin);

        if (texto[0] == '\n' || texto[0] == ' ')
        {
            printf("\nERRO: insira um valor");
        }
    }
    while (texto[0] == '\n' || texto[0] == ' ');

    tamString = strlen(texto);

    if (texto[tamString-1] != '\n')
    {
        limparBuffer();
    }
    else
    {
        texto[tamString-1] = '\0';
    }
}


void limparBuffer(void)
{
    char letra;

    do
    {
        letra = getchar();
    }
    while (letra != '\n' && letra != EOF);
}
