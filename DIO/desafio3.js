class Heroi {
	constructor(nome, idade, tipo) {
	  this.nome = nome;
	  this.idade = idade;
	  this.tipo = tipo;
	}
  
	atacar() {
	  if (this.tipo === 'mago') {
		console.log(`O herói ${this.nome} de ${this.idade} anos e classe ${this.tipo} atacou usando magia!`);
	  } else if (this.tipo === 'guerreiro') {
		console.log(`O herói ${this.nome} de ${this.idade} anos e classe ${this.tipo} atacou usando espada!`);
	  } else if (this.tipo === 'monge') {
		console.log(`O herói ${this.nome} de ${this.idade} anos e classe ${this.tipo} atacou usando artes marciais!`);
	  } else if (this.tipo === 'ninja') {
		console.log(`O herói ${this.nome} de ${this.idade} anos e classe ${this.tipo} atacou usando shuriken!`);
	  }
	}
  }
  
  const nomeHeroi = 'Paulo';
  const idadeHeroi = 22;
  const tipoHeroi = 'ninja';
  
  const heroi = new Heroi(nomeHeroi, idadeHeroi, tipoHeroi);
  
  heroi.atacar();