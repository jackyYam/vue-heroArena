<script setup lang="ts">
import { type HTMLAttributes, computed } from 'vue'
import {
  ProgressIndicator,
  ProgressRoot,
  type ProgressRootProps,
} from 'radix-vue'
import { cn } from '@/lib/utils'

interface ExtendedProgressRootProps extends ProgressRootProps {
  indicatorClass?: string;
}

const props = withDefaults(
  defineProps<ExtendedProgressRootProps & { class?: HTMLAttributes['class'] }>(),
  {
    modelValue: 0,
    indicatorClass: 'bg-primary',
  },
)

const delegatedProps = computed(() => {
  const { class: _, ...delegated } = props

  return delegated
})
</script>

<template>
  <ProgressRoot v-bind="delegatedProps" :class="cn(
    'relative h-4 w-full overflow-hidden rounded-full bg-secondary',
    props.class,
  )
    ">
    <ProgressIndicator :class="cn('h-full w-full flex-1 bg-primary transition-all', props.indicatorClass)"
      :style="`transform: translateX(-${100 - (props.modelValue ?? 0)}%);`" />
  </ProgressRoot>
</template>
