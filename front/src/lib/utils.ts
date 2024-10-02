import { type ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';
import type { Hero, HeroFull } from '@/lib/types';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

function calculateHP(hero: Hero) {
  const { durability, strength, power, AS } = hero.powerstats;
  return (
    ((strength * 0.8 + durability * 0.7 + power) * (1 + AS / 10)) / 2 + 100
  );
}

function calculateFB(hero: Hero, teamAlignment: string) {
  if (teamAlignment === hero.alignment) {
    return 1 + Math.floor(Math.random() * 10);
  } else {
    return 1 / (1 + Math.floor(Math.random() * 10));
  }
}

export const parseHero = (hero: Hero, teamAlignment: string): HeroFull => {
  const { powerstats } = hero;
  const { AS } = powerstats;
  const transformedStats = { ...powerstats };
  const hp = calculateHP(hero);
  const fb = calculateFB(hero, teamAlignment);
  for (const key in transformedStats) {
    if (key !== 'AS') {
      transformedStats[key as keyof typeof powerstats] =
        ((2 * transformedStats[key as keyof typeof powerstats] + AS) * fb) / 2;
    }
  }
  return { ...hero, hp, fb, actualStats: transformedStats };
};

export const getTeamAlignment = (heros: HeroFull[]) => {
  const alignment = heros.reduce((acc, hero) => {
    if (acc[hero.alignment]) {
      acc[hero.alignment]++;
    } else {
      acc[hero.alignment] = 1;
    }
    return acc;
  }, {} as Record<string, number>);
  return Object.keys(alignment).reduce((a, b) =>
    alignment[a] > alignment[b] ? a : b
  );
};
