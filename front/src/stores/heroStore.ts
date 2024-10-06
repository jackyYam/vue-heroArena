import create from 'vue-zustand';
import type { Hero, HeroFull, Team } from '@/lib/types';
import { parseHero, getTeamAlignment } from '@/lib/utils';

interface heroStore {
  heroes: Hero[];
  setHeroes: (heroes: Hero[]) => void;
}

export const useHeroStore = create<heroStore>((set) => ({
  heroes: [],
  setHeroes: (heroes) => set(() => ({ heroes })),
}));

interface gameSettingsStore {
  team1: Team;
  team2: Team;
  setTeam1: (team: Team) => void;
  setTeam2: (team: Team) => void;
}

export const useGameSettingsStore = create<gameSettingsStore>((set) => ({
  team1: { alignment: '', heroes: [] },
  team2: { alignment: '', heroes: [] },
  setTeam1: (team) => set(() => ({ team1: team })),
  setTeam2: (team) => set(() => ({ team2: team })),
}));

interface emailStore {
  email: string;
  setEmail: (email: string) => void;
}

export const useEmailStore = create<emailStore>((set) => ({
  email: '',
  setEmail: (email) => set(() => ({ email })),
}));
