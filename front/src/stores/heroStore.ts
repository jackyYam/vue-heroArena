import create from 'vue-zustand';
import type { Hero, HeroFull, Team } from '@/lib/types';
import { parseHero, getTeamAlignment } from '@/lib/utils';

interface heroStore {
  heroes: Hero[];
  setHeroes: (heroes: Hero[]) => void;
  team1: Team[];
  team2: Team[];
  splitTeams: () => void;
}

export const useHeroStore = create<heroStore>((set) => ({
  heroes: [],
  team1: [],
  team2: [],
  setHeroes: (heroes) => set({ heroes }),
  splitTeams: () => {
    const shuffledHeroes = [...useHeroStore.getState().heroes].sort(
      () => Math.random() - 0.5
    );
    const half = Math.ceil(shuffledHeroes.length / 2);
    const team1 = shuffledHeroes.splice(0, half);
    const team2 = shuffledHeroes;
    set({ team1, team2 });
  },
}));
