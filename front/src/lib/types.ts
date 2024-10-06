interface Powerstats {
  intelligence: number;
  strength: number;
  speed: number;
  durability: number;
  power: number;
  combat: number;
  AS: number;
}

interface Biography {
  'full-name': string;
  'alter-egos': string;
  aliases: string[];
  'place-of-birth': string;
  'first-appearance': string;
  publisher: string;
  alignment: string;
}

export interface Hero {
  id: number;
  name: string;
  powerstats: Powerstats;
  alignment: string;
  biography: Biography;
  image: string;
}

export interface HeroFull extends Hero {
  hp: number;
  fb: number;
  actualStats: Powerstats;
  isbuffed: boolean;
}

export interface Team {
  alignment: string;
  heroes: HeroFull[];
}
