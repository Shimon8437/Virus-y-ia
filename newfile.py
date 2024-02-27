import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Perseguidor Pygame")

# Configuración del objeto principal
lado = 50
objeto_principal_coords = [(200 - lado, 200 + lado),
                           (200, 200 - lado),
                           (200 + lado, 200 + lado)]
color_principal = (255, 0, 0)

# Lista para almacenar los objetos duplicados
objetos_duplicados = []

# Velocidad del objeto principal
velocidad = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Limpiar la lista de objetos duplicados al presionar Enter
                objetos_duplicados = []
                # Cerrar la aplicación al presionar Enter
                pygame.quit()
                sys.exit()

    # Obtener la posición del ratón
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Mover el objeto principal hacia el ratón
    dx = mouse_x - objeto_principal_coords[1][0]
    dy = mouse_y - objeto_principal_coords[1][1]
    distancia = pygame.math.Vector2(dx, dy).length()
    if distancia > 0:
        for i in range(len(objeto_principal_coords)):
            objeto_principal_coords[i] = (objeto_principal_coords[i][0] + velocidad * dx / distancia,
                                           objeto_principal_coords[i][1] + velocidad * dy / distancia)

    # Dibujar el objeto principal como un polígono
    screen.fill((255, 255, 255))
    pygame.draw.polygon(screen, color_principal, objeto_principal_coords)

    # Dibujar y actualizar los objetos duplicados
    for duplicado in objetos_duplicados:
        pygame.draw.polygon(screen, (0, 0, 255), duplicado)

    # Verificar si el objeto principal toca el ratón y duplicarlo
    if pygame.Rect(objeto_principal_coords[1][0] - lado/2, objeto_principal_coords[1][1] - lado/2, lado, lado).collidepoint(mouse_x, mouse_y):
        nuevo_duplicado_coords = [(coord[0] - lado/2, coord[1] - lado/2) for coord in objeto_principal_coords]
        objetos_duplicados.append(nuevo_duplicado_coords)

    pygame.display.flip()
    pygame.time.Clock().tick(60)