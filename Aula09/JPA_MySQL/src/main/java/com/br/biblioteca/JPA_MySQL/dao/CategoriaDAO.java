package com.br.biblioteca.JPA_MySQL.dao;

import com.br.biblioteca.JPA_MySQL.log.Log;
import com.br.biblioteca.JPA_MySQL.model.Categoria;

import java.io.IOException;
import javax.persistence.EntityManager;

public class CategoriaDAO {

    private EntityManager em;

    //Criando instância do Logger
    Log meuLogger = new Log("Log.txt");

    //Contrutor por atribuir o EntityManager vindo como parâmetro para o atributo em da classe local
    public CategoriaDAO(EntityManager em) throws IOException {
        this.em = em;
    }

    //Método responsável por cadastrar uma categoria no banco de dados
    public void cadastrar(Categoria categoria) {
        this.em.persist(categoria);
        System.out.println("\nA categoria '" + categoria.getNome() + "' foi criada com sucesso!\n");
        meuLogger.logger.info("\nA categoria '" + categoria.getNome() + "' foi criada na base de dados!\n");
    }

}
