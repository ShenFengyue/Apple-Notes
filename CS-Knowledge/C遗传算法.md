# 这是一段C语言遗传算法

```C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 定义种群大小和染色体长度
#define POPULATION_SIZE 10
#define GENE_LENGTH 5

// 定义交叉率和变异率
#define CROSSOVER_RATE 0.7
#define MUTATION_RATE 0.1

// 初始化种群
void init_population(int population[][GENE_LENGTH]) {
    int i, j;
    for (i = 0; i < POPULATION_SIZE; i++) {
        for (j = 0; j < GENE_LENGTH; j++) {
            population[i][j] = rand() % 2;
        }
    }
}

// 计算染色体的适应度
int calculate_fitness(int chromosome[]) {
    int i, fitness = 0;
    for (i = 0; i < GENE_LENGTH; i++) {
        fitness += chromosome[i];
    }
    return fitness;
}

// 选择操作
void selection(int population[][GENE_LENGTH], int selected_population[][GENE_LENGTH]) {
    int i, j, k;
    int fitness_list[POPULATION_SIZE];
    int total_fitness = 0;
    double probability_list[POPULATION_SIZE];
    double roulette_wheel[POPULATION_SIZE];
    double cum_probability = 0;
    for (i = 0; i < POPULATION_SIZE; i++) {
        fitness_list[i] = calculate_fitness(population[i]);
        total_fitness += fitness_list[i];
    }
    for (i = 0; i < POPULATION_SIZE; i++) {
        probability_list[i] = (double) fitness_list[i] / total_fitness;
    }
    for (i = 0; i < POPULATION_SIZE; i++) {
        cum_probability += probability_list[i];
        roulette_wheel[i] = cum_probability;
    }
    for (i = 0; i < POPULATION_SIZE; i++) {
        double random_number = (double) rand() / RAND_MAX;
        for (j = 0; j < POPULATION_SIZE; j++) {
            if (random_number <= roulette_wheel[j]) {
                for (k = 0; k < GENE_LENGTH; k++) {
                    selected_population[i][k] = population[j][k];
                }
                break;
            }
        }
    }
}

// 交叉操作
void crossover(int parent1[], int parent2[], int child1[], int child2[]) {
    int i, crossover_point;
    double random_number = (double) rand() / RAND_MAX;
    if (random_number < CROSSOVER_RATE) {
        crossover_point = rand() % GENE_LENGTH;
        for (i = 0; i < crossover_point; i++) {
            child1[i] = parent1[i];
            child2[i] = parent2[i];
        }
        for (i = crossover_point; i < GENE_LENGTH; i++) {
            child1[i] = parent2[i];
            child2[i] = parent1[i];
        }
    }
    else {
        for (i = 0; i < GENE_LENGTH; i++) {
            child1[i] = parent1[i];
            child2[i] = parent2[i];
        }
    }
}

// 变异操作
void mutation(int chromosome[]) {
    int i;
    double random_number = (double) rand() / RAND_MAX;
    if (random_number < MUTATION_RATE) {
        int mutation_point = rand() % GENE_LENGTH;
        chromosome[mutation_point] = !chromosome[mutation_point];
    }
}

// 遗传算法主函数
int main() {
    int population[POPULATION_SIZE][GENE_LENGTH];
    int selected_population[POPULATION_SIZE][GENE_LENGTH];
    int offspring_population[POPULATION_SIZE][GENE_LENGTH];
    int i, j;

    srand(time(NULL)); // 随机种子

    // 初始化种群
    init_population(population);

    // 迭代
    for (i = 0; i < 100; i++) {
        // 选择
        selection(population, selected_population);

        // 交叉
        for (j = 0; j < POPULATION_SIZE; j += 2) {
            crossover(selected_population[j], selected_population[j+1], 
                      offspring_population[j], offspring_population[j+1]);
        }

        // 变异
        for (j = 0; j < POPULATION_SIZE; j++) {
            mutation(offspring_population[j]);
        }

        // 将后代种群复制到当前种群中
        for (j = 0; j < POPULATION_SIZE; j++) {
            for (int k = 0; k < GENE_LENGTH; k++) {
                population[j][k] = offspring_population[j][k];
            }
        }
    }
    return 0;
}

```
